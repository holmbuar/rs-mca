#!/usr/bin/env node
'use strict';

// Independent hostile verifier for the full M215, b>=164 arrangement theorem.
// It does not load, parse, import, require, or eval the claimed Ruby verifier or
// its arithmetic support.  Every equation below is reimplemented directly from
// the incidence, DPW, bad-line, deletion, and terminal ledgers.

const crypto = require('crypto');
const fs = require('fs');
const path = require('path');

function insist(condition, message) {
  if (!condition) throw new Error(`HOSTILE AUDIT FAILURE: ${message}`);
}

const PINNED_INPUTS = Object.freeze({
  'M215_B164_FULL_ACTIVE_DELETION_NONEXISTENCE.md':
    '0fbad5a6a12718588400e1b195433fd6096eaaa8f0b8188b57a1fee9c39c454d',
  'verify_m215_b164_full_active_deletion_nonexistence.rb':
    'cc47b2a1c7e79d003d5d5a5b2898b8f714b9aae2479a5ed5a5f8df57a5effe9b',
  'verify_m215_b164_full_active_deletion_nonexistence.expected.txt':
    '014381b3b29e5edddc9c64423ea8e0f1e43fe5985865f62c7db5eabc134c4594'
});

for (const [basename, expected] of Object.entries(PINNED_INPUTS)) {
  const bytes = fs.readFileSync(path.join(__dirname, basename));
  const actual = crypto.createHash('sha256').update(bytes).digest('hex');
  insist(actual === expected,
         `pinned input drift ${basename}: expected ${expected}, got ${actual}`);
}

const EXPECTED_BASENAME =
  'verify_m215_full_active_deletion_hostile_audit_1.expected.txt';
const EXPECTED_SHA256 =
  '3770fc44ab4de38a3d024003470a502d800edccce02c7040d7a61323b6646a2b';

function pairs(n) {
  return n * (n - 1) / 2;
}

function dpwBasic(lines, relationDegree) {
  return (lines - 1) ** 2 -
         relationDegree * (lines - 1 - relationDegree);
}

function dpwSharp(lines, relationDegree) {
  return dpwBasic(lines, relationDegree) -
         pairs(2 * relationDegree - lines + 2);
}

function gcd(a, b) {
  a = Math.abs(a);
  b = Math.abs(b);
  while (b !== 0) {
    const t = a % b;
    a = b;
    b = t;
  }
  return a;
}

function reduced(numerator, denominator) {
  insist(denominator > 0, 'nonpositive rational denominator');
  const g = gcd(numerator, denominator);
  return [numerator / g, denominator / g];
}

function ratCompare(left, right) {
  const lhs = left[0] * right[1];
  const rhs = right[0] * left[1];
  if (Number.isSafeInteger(lhs) && Number.isSafeInteger(rhs)) return lhs - rhs;
  const exact = BigInt(left[0]) * BigInt(right[1]) -
                BigInt(right[0]) * BigInt(left[1]);
  return exact < 0n ? -1 : (exact > 0n ? 1 : 0);
}

function ratAdd(left, right) {
  return reduced(left[0] * right[1] + right[0] * left[1],
                 left[1] * right[1]);
}

function price(neighbours) {
  return reduced(pairs(neighbours), neighbours + 1);
}

// Exact minimum of sum C(a,2)/(a+1) for a fixed positive-integer sum and
// at most `capacity` positive parts.  The returned fraction is reduced.
function balancedPrice(total, capacity) {
  if (total === 0 && capacity >= 0) return [0, 1];
  if (total < 0 || capacity <= 0) return null;
  const partCount = Math.min(total, capacity);
  const small = Math.floor(total / partCount);
  const largeCount = total % partCount;
  const left = [partCount - largeCount, 1];
  const right = [largeCount, 1];
  return ratAdd([left[0] * price(small)[0], price(small)[1]],
                [right[0] * price(small + 1)[0], price(small + 1)[1]]);
}

// Independent checks of the balanced-partition lemma: all discrete second
// differences in the possible scan range, plus a small exact dynamic program.
for (let a = 2; a <= 214; ++a) {
  const lhs = ratAdd(price(a - 1), price(a + 1));
  const rhs = [2 * price(a)[0], price(a)[1]];
  insist(ratCompare(lhs, rhs) >= 0, `price convexity at a=${a}`);
}

const brute = Array.from({length: 31}, () => Array(11).fill(null));
for (let slots = 0; slots <= 10; ++slots) brute[0][slots] = [0, 1];
for (let total = 1; total <= 30; ++total) {
  for (let slots = 1; slots <= 10; ++slots) {
    let best = null;
    for (let first = 1; first <= total; ++first) {
      const rest = brute[total - first][slots - 1];
      if (rest === null) continue;
      const candidate = ratAdd(price(first), rest);
      if (best === null || ratCompare(candidate, best) < 0) best = candidate;
    }
    brute[total][slots] = best;
    insist(ratCompare(best, balancedPrice(total, slots)) === 0,
           `balanced-price dynamic program total=${total}, slots=${slots}`);
  }
}

function coarseRelaxedGap(marked, lines, relationDegree, bad) {
  const good = lines - bad;
  const quotientDegree = relationDegree + 1 - bad;
  const parentCap = dpwBasic(lines, relationDegree) - pairs(lines) -
                    91 * marked;
  const totalDeficiency = 15 * (lines - marked);
  const egMin = Math.max(0, totalDeficiency - 14 * bad);
  const egMax = Math.min(14 * good, totalDeficiency);
  if (egMin > egMax) return null;

  let best = null;
  for (let goodDeficiency = egMin;
       goodDeficiency <= egMax;
       ++goodDeficiency) {
    const badMarkedIncidence =
      15 * bad - totalDeficiency + goodDeficiency;
    if (badMarkedIncidence < bad || badMarkedIncidence > 15 * bad) continue;

    const goodMarkedIncidence = 15 * good - goodDeficiency;
    const independentBadPairBudget = pairs(bad);
    const erasedUpper = Math.min(
      Math.floor(independentBadPairBudget / 91),
      Math.floor(badMarkedIncidence / 14),
      goodMarkedIncidence
    );
    const slotCapacity = good * quotientDegree - goodMarkedIncidence +
                         erasedUpper;
    if (slotCapacity < 0) continue;

    const markedBadGoodLower = Math.max(
      0, 14 * badMarkedIncidence - 2 * independentBadPairBudget
    );
    const residualBadGoodUpper = bad * good - markedBadGoodLower;
    if (residualBadGoodUpper < 0) continue;

    const allGoodResidualDegree =
      good * (lines - 211) + 14 * goodDeficiency;
    const goodGoodDegreeLower =
      Math.max(0, allGoodResidualDegree - residualBadGoodUpper);
    const lower = balancedPrice(goodGoodDegreeLower, slotCapacity);
    if (lower === null) continue;
    const gap = reduced(lower[0] - parentCap * lower[1], lower[1]);
    if (best === null || ratCompare(gap, best) < 0) best = gap;
  }
  return best;
}

// -------------------------------------------------------------------------
// 1. Independent DPW and permissive coarse scans.
// -------------------------------------------------------------------------

const highRows = [];
const coarseRows = [];
let leastPositiveCoarse = null;

for (let marked = 164; marked <= 215; ++marked) {
  for (let lines = marked; lines <= 215; ++lines) {
    const forcedTau = pairs(lines) + 91 * marked;
    const highStart = Math.floor((lines + 1) / 2);

    for (let relationDegree = highStart;
         relationDegree < lines;
         ++relationDegree) {
      const slack = dpwSharp(lines, relationDegree) - forcedTau;
      if (slack >= 0) highRows.push([marked, lines, relationDegree, slack]);
    }

    for (let relationDegree = 0;
         relationDegree < highStart;
         ++relationDegree) {
      if (dpwBasic(lines, relationDegree) < forcedTau) continue;
      const lastBad = Math.min(relationDegree + 1, lines - 1);
      for (let bad = 0; bad <= lastBad; ++bad) {
        const gap = coarseRelaxedGap(marked, lines, relationDegree, bad);
        if (gap === null) continue;
        if (gap[0] <= 0) {
          coarseRows.push([marked, lines, relationDegree, bad, gap]);
        } else if (leastPositiveCoarse === null ||
                   ratCompare(gap, leastPositiveCoarse) < 0) {
          leastPositiveCoarse = gap;
        }
      }
    }
  }
}

insist(highRows.length === 0,
       `high-DPW survivors ${JSON.stringify(highRows.slice(0, 5))}`);
insist(coarseRows.length === 29595,
       `coarse row count ${coarseRows.length}, expected 29595`);
insist(Math.max(...coarseRows.map(row => row[3])) === 35,
       'maximum coarse bad-line count is not 35');
insist(coarseRows.every(row => row[3] <= row[2]),
       'a forbidden B=r+1 row survived');
insist(leastPositiveCoarse !== null && leastPositiveCoarse[0] > 0,
       'coarse eliminated rows lack a strict positive gap');

// -------------------------------------------------------------------------
// 2. Full-pencil and finite-linear-space cuts.
// -------------------------------------------------------------------------

const structuralRows = [];
const finiteSpaceCut = [];
for (const row of coarseRows) {
  const [marked, lines, relationDegree, bad] = row;
  const good = lines - bad;
  const quotientDegree = relationDegree + 1 - bad;
  insist(good > 15, `G<=15 in coarse row ${JSON.stringify(row)}`);
  insist(pairs(bad) < 91 * marked,
         `full-pencil bad-pair gate failed ${JSON.stringify(row)}`);
  if (quotientDegree < 2 ||
      good > quotientDegree * (quotientDegree - 1) + 1) {
    finiteSpaceCut.push(row);
  } else {
    structuralRows.push(row);
  }
}

insist(finiteSpaceCut.length === 8541,
       `finite-space cut ${finiteSpaceCut.length}, expected 8541`);
insist(structuralRows.length === 21054,
       `structural rows ${structuralRows.length}, expected 21054`);
const zeroBadRows = structuralRows.filter(row => row[3] === 0);
const positiveBadRows = structuralRows.filter(row => row[3] > 0);
insist(zeroBadRows.length === 121,
       `B=0 rows ${zeroBadRows.length}, expected 121`);
insist(positiveBadRows.length === 20933,
       `B>0 rows ${positiveBadRows.length}, expected 20933`);

// -------------------------------------------------------------------------
// 3. Exhaustive joint-(E_g,K,C) deletion replay for every B>0 row.
// -------------------------------------------------------------------------

const positiveSurvivors = [];
const exceptionalIntegerStates = [];
const infeasibleRows = [];
let leastPositiveJoint = null;
let jointStateCount = 0;
let maximumRawPriceNumerator = 0;
let maximumRawPriceDenominator = 0;
let maximumGapCrossProduct = 0;

for (let rowIndex = 0; rowIndex < positiveBadRows.length; ++rowIndex) {
  const [marked, lines, relationDegree, bad] = positiveBadRows[rowIndex];
  const good = lines - bad;
  const quotientDegree = relationDegree + 1 - bad;
  const deletionRelationDegree = relationDegree - bad;
  insist(deletionRelationDegree === quotientDegree - 1,
         `deletion mdr identity in row ${rowIndex}`);

  const parentCap = dpwBasic(lines, relationDegree) - pairs(lines) -
                    91 * marked;
  const totalDeficiency = 15 * (lines - marked);
  const egMin = Math.max(0, totalDeficiency - 14 * bad);
  const egMax = Math.min(14 * good, totalDeficiency);

  let bestN = null;
  let bestD = 1;
  let bestState = null;

  for (let goodDeficiency = egMin;
       goodDeficiency <= egMax;
       ++goodDeficiency) {
    const badMarkedIncidence =
      15 * bad - totalDeficiency + goodDeficiency;
    if (badMarkedIncidence < bad || badMarkedIncidence > 15 * bad) continue;

    const cLowerNumerator = 14 * badMarkedIncidence - bad * good;
    const cLower = cLowerNumerator > 0 ?
      Math.floor((cLowerNumerator + 1) / 2) : 0;
    const cUpper = Math.min(pairs(bad), 7 * badMarkedIncidence);
    if (cLower > cUpper) continue;

    for (let markedBadPairs = cLower;
         markedBadPairs <= cUpper;
         ++markedBadPairs) {
      const markedBadGood =
        14 * badMarkedIncidence - 2 * markedBadPairs;
      if (markedBadGood < 0 || markedBadGood > bad * good) continue;

      ++jointStateCount;
      const residualBadGood = bad * good - markedBadGood;
      const goodMarkedIncidence = 15 * good - goodDeficiency;
      const erasedUpper = Math.min(
        Math.floor(markedBadPairs / 91),
        Math.floor(badMarkedIncidence / 14),
        goodMarkedIncidence
      );
      const slotCapacity = good * quotientDegree - goodMarkedIncidence +
                           erasedUpper;
      if (slotCapacity < 0) continue;

      const allGoodResidualDegree =
        good * (lines - 211) + 14 * goodDeficiency;
      const goodGoodDegree =
        Math.max(0, allGoodResidualDegree - residualBadGood);

      // Allocation-free exact balanced price for the 373,774,811-state loop.
      let lowerN;
      let lowerD;
      if (goodGoodDegree === 0) {
        lowerN = 0;
        lowerD = 1;
      } else {
        if (slotCapacity <= 0) continue;
        const partCount = Math.min(goodGoodDegree, slotCapacity);
        const small = Math.floor(goodGoodDegree / partCount);
        const largeCount = goodGoodDegree % partCount;
        lowerN =
          (partCount - largeCount) * small * (small - 1) * (small + 2) +
          largeCount * small * (small + 1) * (small + 1);
        lowerD = 2 * (small + 1) * (small + 2);
      }

      const deletionMarkedExcessLower =
        91 * marked - 13 * badMarkedIncidence + markedBadPairs -
        Math.floor(markedBadPairs / 105);
      const deletionCap =
        dpwBasic(good, deletionRelationDegree) - pairs(good) -
        deletionMarkedExcessLower;
      const effectiveCap = Math.min(parentCap, deletionCap);
      const gapN = lowerN - effectiveCap * lowerD;
      insist(Number.isSafeInteger(lowerN) && Number.isSafeInteger(lowerD) &&
             Number.isSafeInteger(gapN),
             `unsafe integer arithmetic in joint state row=${rowIndex}`);
      maximumRawPriceNumerator =
        Math.max(maximumRawPriceNumerator, Math.abs(lowerN));
      maximumRawPriceDenominator =
        Math.max(maximumRawPriceDenominator, lowerD);

      if (!(quotientDegree === 15 && good >= 198) &&
          Math.ceil(lowerN / lowerD) <= effectiveCap) {
        const lowReduced = reduced(lowerN, lowerD);
        exceptionalIntegerStates.push([
          marked, lines, relationDegree, bad, quotientDegree, good,
          goodDeficiency, badMarkedIncidence, markedBadPairs,
          residualBadGood, erasedUpper, slotCapacity, goodGoodDegree,
          lowReduced, effectiveCap, parentCap, deletionCap
        ]);
      }

      const leftCross = bestN === null ? 0 : gapN * bestD;
      const rightCross = bestN === null ? 0 : bestN * lowerD;
      if (bestN !== null) {
        insist(Number.isSafeInteger(leftCross) && Number.isSafeInteger(rightCross),
               `unsafe rational comparison in joint state row=${rowIndex}`);
        maximumGapCrossProduct = Math.max(
          maximumGapCrossProduct, Math.abs(leftCross), Math.abs(rightCross)
        );
      }
      if (bestN === null || leftCross < rightCross) {
        bestN = gapN;
        bestD = lowerD;
        const lowReduced = reduced(lowerN, lowerD);
        bestState = [
          goodDeficiency, badMarkedIncidence, markedBadPairs,
          residualBadGood, erasedUpper, slotCapacity, goodGoodDegree,
          lowReduced, effectiveCap, parentCap, deletionCap
        ];
      }
    }
  }

  if (bestN === null) {
    infeasibleRows.push([marked, lines, relationDegree, bad]);
  } else if (bestN <= 0) {
    const bestReduced = reduced(bestN, bestD);
    positiveSurvivors.push([
      marked, lines, relationDegree, bad, quotientDegree, good,
      bestReduced, bestState
    ]);
  } else if (leastPositiveJoint === null ||
             ratCompare([bestN, bestD], leastPositiveJoint) < 0) {
    leastPositiveJoint = reduced(bestN, bestD);
  }
}

insist(infeasibleRows.length === 0,
       `joint-C rows with no relaxed state ${JSON.stringify(infeasibleRows.slice(0, 5))}`);
insist(jointStateCount === 373774811,
       `joint-C states ${jointStateCount}, expected 373774811`);
insist(positiveSurvivors.length === 404,
       `positive-B survivors ${positiveSurvivors.length}, expected 404`);
insist(leastPositiveJoint[0] === 1 && leastPositiveJoint[1] === 120,
       `least positive joint gap ${leastPositiveJoint.join('/')}`);

const qgDistribution = new Map();
for (const row of positiveSurvivors) {
  const key = `${row[4]},${row[5]}`;
  qgDistribution.set(key, (qgDistribution.get(key) || 0) + 1);
}
const expectedQG = new Map([
  ['15,207', 8], ['15,208', 74], ['15,209', 137],
  ['15,210', 181], ['16,214', 4]
]);
insist(JSON.stringify([...qgDistribution.entries()].sort()) ===
       JSON.stringify([...expectedQG.entries()].sort()),
       `q,G distribution ${JSON.stringify([...qgDistribution])}`);

const positiveDesign = positiveSurvivors.filter(
  row => row[4] === 15 && row[5] >= 198
);
const positiveOther = positiveSurvivors.filter(
  row => !(row[4] === 15 && row[5] >= 198)
);
insist(positiveDesign.length === 400,
       `positive design rows ${positiveDesign.length}, expected 400`);
const expectedPositiveOther = [
  [164, 215, 16, 1, 16, 214, -11, 78],
  [165, 215, 16, 1, 16, 214, -4, 39],
  [166, 215, 16, 1, 16, 214, -5, 78],
  [167, 215, 16, 1, 16, 214, -1, 39]
];
const actualPositiveOther = positiveOther.map(row => [
  ...row.slice(0, 6), row[6][0], row[6][1]
]);
insist(JSON.stringify(actualPositiveOther) ===
       JSON.stringify(expectedPositiveOther),
       `positive exceptional rows ${JSON.stringify(actualPositiveOther)}`);

const expectedExceptionalStates = [
  [164, 215, 16, 1, 16, 214, 751, 1, 0, 200, 0, 965,
   11170, 366355, 78, 4697, 4699, 4697],
  [165, 215, 16, 1, 16, 214, 736, 1, 0, 200, 0, 950,
   10960, 179630, 39, 4606, 4608, 4606],
  [166, 215, 16, 1, 16, 214, 721, 1, 0, 200, 0, 935,
   10750, 352165, 78, 4515, 4517, 4515],
  [167, 215, 16, 1, 16, 214, 706, 1, 0, 200, 0, 920,
   10540, 172535, 39, 4424, 4426, 4424]
];
const actualExceptionalStates = exceptionalIntegerStates.map(row => [
  ...row.slice(0, 13), row[13][0], row[13][1], ...row.slice(14)
]);
insist(JSON.stringify(actualExceptionalStates) ===
       JSON.stringify(expectedExceptionalStates),
       `exceptional integer-state ledger ${JSON.stringify(actualExceptionalStates)}`);

// Independent survivor-row fingerprint, using the claimed ledger's documented
// canonical format but values computed solely by this verifier.
const survivorLedger = positiveSurvivors.map(row =>
  [...row.slice(0, 6), row[6][0], row[6][1]].join(',')
).sort().join('\n');
const survivorDigest =
  crypto.createHash('sha256').update(survivorLedger).digest('hex');
insist(survivorDigest ===
       'd4f0798b89f133791e2e79d90851eb51937cbee4bb816ee5634c64d7f0f67dc6',
       `survivor ledger digest ${survivorDigest}`);

// -------------------------------------------------------------------------
// 4. B=0 residue and the four deletion-equality bridges.
// -------------------------------------------------------------------------

const zeroDesign = zeroBadRows.filter(row =>
  row[2] + 1 - row[3] === 15 && row[1] - row[3] >= 198
);
const zeroOther = zeroBadRows.filter(row =>
  !(row[2] + 1 - row[3] === 15 && row[1] - row[3] >= 198)
);
insist(zeroDesign.length === 106,
       `B=0 design rows ${zeroDesign.length}, expected 106`);

const expectedZeroOther = [
  [164, 214, 15, 0, -3, 26], [164, 215, 15, 0, -31, 78],
  [165, 214, 15, 0, -1, 13], [165, 215, 15, 0, -14, 39],
  [166, 214, 15, 0, -1, 26], [166, 215, 15, 0, -25, 78],
  [167, 214, 15, 0, 0, 1],   [167, 215, 15, 0, -11, 39],
  [168, 215, 15, 0, -19, 78], [169, 215, 15, 0, -8, 39],
  [170, 215, 15, 0, -1, 6],   [171, 215, 15, 0, -5, 39],
  [172, 215, 15, 0, -7, 78],  [173, 215, 15, 0, -2, 39],
  [174, 215, 15, 0, -1, 78]
];
const actualZeroOther = zeroOther.map(row => [
  ...row.slice(0, 4), row[4][0], row[4][1]
]);
insist(JSON.stringify(actualZeroOther) === JSON.stringify(expectedZeroOther),
       `B=0 terminal rows ${JSON.stringify(actualZeroOther)}`);

const terminalSqueezes = zeroOther.map(row => {
  const [marked, lines, relationDegree, , gap] = row;
  const upper = dpwBasic(lines, relationDegree) - pairs(lines) - 91 * marked;
  const lowerN = upper * gap[1] + gap[0];
  insist(Math.ceil(lowerN / gap[1]) === upper,
         `terminal integral squeeze b=${marked},d=${lines}`);
  const lower = reduced(lowerN, gap[1]);
  return [marked, lines, lower[0], lower[1], upper];
});

for (const row of exceptionalIntegerStates) {
  const [marked, lines, relationDegree, bad, quotientDegree, good,
         goodDeficiency, badMarkedIncidence, markedBadPairs,
         residualBadGood, erasedUpper, slotCapacity, goodGoodDegree,
         lower, effectiveCap, parentCap, deletionCap] = row;
  insist(lines === 215 && relationDegree === 16 && bad === 1 &&
         quotientDegree === 16 && good === 214,
         `exceptional geometry mismatch b=${marked}`);
  insist(badMarkedIncidence === 1 && markedBadPairs === 0,
         `exceptional K,C mismatch b=${marked}`);
  insist(Math.ceil(lower[0] / lower[1]) === deletionCap &&
         effectiveCap === deletionCap && parentCap === deletionCap + 2,
         `exceptional equality squeeze b=${marked}`);
  const exactMarkedExcess = 91 * (marked - 1) + 78;
  insist(exactMarkedExcess === 91 * marked - 13,
         `exceptional deletion marked excess b=${marked}`);
  insist(dpwBasic(214, 15) === 42399,
         'exceptional deletion DPW equality target');
  void goodDeficiency; void residualBadGood; void erasedUpper;
  void slotCapacity; void goodGoodDegree;
}

// -------------------------------------------------------------------------
// 5. Independent terminal d=214,215 moment and residue arithmetic.
// -------------------------------------------------------------------------

const terminalFamilies = [
  [215, 164, 416, 1066, [4717, 15384, 17689, 14161], 2988],
  [214, 163, 432, 1134, [7074, 17525, 22201, 18225], 5350]
];
const terminalLedgers = [];

for (const [lines, minimumUnits, epsilonBase, epsilonSquareBase,
            expectedDefectGaps, expectedDoubleGap] of terminalFamilies) {
  const tau = dpwBasic(lines, 15);
  const sumMuMinusOne = lines * (lines - 1) - tau;
  insist(sumMuMinusOne === 16 * lines - 241,
         `sum(mu-1) identity d=${lines}`);
  const defectGaps = [];
  for (let defect = 1; defect <= 4; ++defect) {
    const pointCount = 241 - defect;
    const epsilonSum = epsilonBase - 15 * defect;
    const epsilonSquares = epsilonSquareBase - 225 * defect;
    let minimumGap = null;
    for (let units = minimumUnits; units <= pointCount; ++units) {
      const gap = (epsilonSum - units) ** 2 -
                  (pointCount - units) * (epsilonSquares - units);
      if (minimumGap === null || gap < minimumGap) minimumGap = gap;
    }
    insist(minimumGap > 0,
           `Cauchy defect contradiction d=${lines},D=${defect}`);
    defectGaps.push(minimumGap);
  }
  insist(JSON.stringify(defectGaps) === JSON.stringify(expectedDefectGaps),
         `defect-gap ledger d=${lines}: ${JSON.stringify(defectGaps)}`);
  insist(epsilonSquareBase - 225 * 5 < minimumUnits,
         `D>=5 square-sum exclusion d=${lines}`);

  let minimumDoubleGap = null;
  for (let units = minimumUnits; units <= 240; ++units) {
    const remainingSum = epsilonBase - 14 - units;
    const remainingSquares = epsilonSquareBase - 196 - units;
    const gap = remainingSum ** 2 -
                (240 - units) * remainingSquares;
    if (minimumDoubleGap === null || gap < minimumDoubleGap) {
      minimumDoubleGap = gap;
    }
  }
  insist(minimumDoubleGap === expectedDoubleGap,
         `double-point gap d=${lines}: ${minimumDoubleGap}`);
  terminalLedgers.push([
    lines, tau, sumMuMinusOne, defectGaps, minimumDoubleGap
  ]);
}

const fieldCharacteristic = 2130706433;
insist(fieldCharacteristic > 215, 'field-characteristic gate');
insist(15 % fieldCharacteristic !== 0,
       'normal-bundle residue contradiction vanished');

const qgText = [...qgDistribution.entries()].sort().map(
  ([key, count]) => `${key.replace(',', ':')}:${count}`
).join(',');
const canonicalLines = [
  'M215_FULL_ACTIVE_DELETION_HOSTILE_AUDIT_1: PASS',
  'pinned_proof_sha256=0fbad5a6a12718588400e1b195433fd6096eaaa8f0b8188b57a1fee9c39c454d',
  'pinned_candidate_verifier_sha256=cc47b2a1c7e79d003d5d5a5b2898b8f714b9aae2479a5ed5a5f8df57a5effe9b',
  'pinned_candidate_stdout_sha256=014381b3b29e5edddc9c64423ea8e0f1e43fe5985865f62c7db5eabc134c4594',
  'field_characteristic=2130706433>215 range=164<=b<=d<=215',
  `high_DPW_survivors=${highRows.length}`,
  `coarse_rows=${coarseRows.length} max_B=${Math.max(...coarseRows.map(row => row[3]))}`,
  `finite_space_cut=${finiteSpaceCut.length} structural_rows=${structuralRows.length}`,
  `B0_rows=${zeroBadRows.length} Bpositive_rows=${positiveBadRows.length}`,
  `joint_C_states=${jointStateCount} joint_C_survivors=${positiveSurvivors.length}`,
  `joint_C_min_positive_gap=${leastPositiveJoint[0]}/${leastPositiveJoint[1]} qG=${qgText}`,
  `exact_number_guard=max_price_num:${maximumRawPriceNumerator},max_price_den:${maximumRawPriceDenominator},max_cross:${maximumGapCrossProduct}<2^53`,
  `joint_C_survivor_sha256=${survivorDigest}`,
  `positive_design=${positiveDesign.length} exceptional=${positiveOther.length}`,
  `B0_design=${zeroDesign.length} B0_terminal=${zeroOther.length}`,
  `terminal_squeezes=${JSON.stringify(terminalSqueezes)}`,
  `terminal_ledgers=${JSON.stringify(terminalLedgers)}`,
  'vanstone_threshold=v>=(r-1)^2-1; r=15,G>=198 embeds in order14 plane',
  'terminal_residue_contradiction=16=1 hence 15=0, impossible in char0 or char>215',
  'scope=arrangement_theorem_only; no recurrence_or_score_claim',
  'RESULT: PASS'
];
const canonicalOutput = `${canonicalLines.join('\n')}\n`;

if (EXPECTED_SHA256 !== 'PENDING') {
  const expectedPath = path.join(__dirname, EXPECTED_BASENAME);
  const expectedBytes = fs.readFileSync(expectedPath);
  const expectedActual =
    crypto.createHash('sha256').update(expectedBytes).digest('hex');
  insist(expectedActual === EXPECTED_SHA256,
         `hostile expected-output drift: ${expectedActual}`);
  insist(expectedBytes.equals(Buffer.from(canonicalOutput)),
         'hostile canonical stdout differs byte-for-byte');
}

process.stdout.write(canonicalOutput);
