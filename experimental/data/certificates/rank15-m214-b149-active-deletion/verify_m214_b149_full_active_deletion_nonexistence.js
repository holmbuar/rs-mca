#!/usr/bin/env node
'use strict';

// Exact primary verifier for the active-deletion theorem
//   149 <= b <= d <= 214,
// with every marked point incident to exactly fifteen arrangement lines.
//
// The arithmetic engine is the source-pinned, independently implemented JS
// engine from the already audited M215 theorem.  This file changes only the
// theorem domain and frozen expected ledgers, then adds the new terminal and
// order-13 subplane checks.  It never loads the Ruby claimant verifier.

const crypto = require('crypto');
const fs = require('fs');
const path = require('path');

const BASE_BASENAME =
  'verify_m215_full_active_deletion_hostile_audit_1.js';
const BASE_SHA256 =
  'c18dd312c08fcde82f68cd6ad7936ee7b367be4b5971d0c65f0a91d28be04549';
const EXPECTED_BASENAME =
  'verify_m214_b149_full_active_deletion_nonexistence.expected.txt';
const EXPECTED_SHA256 =
  'b0ce72c80199b9f3504c1bad570077630591b70303e56d9bd2dab8cef53dc923';

function sha256(bytes) {
  return crypto.createHash('sha256').update(bytes).digest('hex');
}

const basePath = path.join(__dirname, BASE_BASENAME);
const baseBytes = fs.readFileSync(basePath);
if (sha256(baseBytes) !== BASE_SHA256) {
  throw new Error('FAIL: frozen independent arithmetic engine drift');
}
let source = baseBytes.toString('utf8').replace(/^#![^\n]*\n/, '');

function replaceOnce(oldText, newText, label) {
  const first = source.indexOf(oldText);
  if (first < 0 || source.indexOf(oldText, first + oldText.length) >= 0) {
    throw new Error(`FAIL: unique transformation drift: ${label}`);
  }
  source = source.slice(0, first) + newText +
           source.slice(first + oldText.length);
}

replaceOnce(
  "for (let marked = 164; marked <= 215; ++marked) {\n  for (let lines = marked; lines <= 215; ++lines) {",
  "for (let marked = 149; marked <= 214; ++marked) {\n  for (let lines = marked; lines <= 214; ++lines) {",
  'theorem domain'
);
replaceOnce(
  'insist(coarseRows.length === 29595,',
  'insist(coarseRows.length === 84460,',
  'coarse-row count'
);
replaceOnce(
  "insist(Math.max(...coarseRows.map(row => row[3])) === 35,\n       'maximum coarse bad-line count is not 35');",
  "insist(Math.max(...coarseRows.map(row => row[3])) === 46,\n       'maximum coarse bad-line count is not 46');",
  'maximum bad-line count'
);
replaceOnce(
  'insist(finiteSpaceCut.length === 8541,',
  'insist(finiteSpaceCut.length === 23635,',
  'finite-space cut count'
);
replaceOnce(
  'insist(structuralRows.length === 21054,',
  'insist(structuralRows.length === 60825,',
  'structural-row count'
);
replaceOnce(
  'insist(zeroBadRows.length === 121,',
  'insist(zeroBadRows.length === 211,',
  'zero-bad-row count'
);
replaceOnce(
  'insist(positiveBadRows.length === 20933,',
  'insist(positiveBadRows.length === 60614,',
  'positive-bad-row count'
);

const postScan = String.raw`
// -------------------------------------------------------------------------
// M214 frozen survivor stratification and terminal reductions.
// -------------------------------------------------------------------------

insist(infeasibleRows.length === 0,
       'joint-C scan contains an infeasible relaxed row');
insist(jointStateCount === 2411034031,
       'joint-C state count is not 2,411,034,031');
insist(positiveSurvivors.length === 685,
       'positive-B survivor count is not 685');
insist(leastPositiveJoint[0] === 1 && leastPositiveJoint[1] === 120,
       'least positive joint gap is not 1/120');

const m214PositiveDesign = positiveSurvivors.filter(
  row => row[4] === 15 && row[5] >= 198
);
const m214PositiveOther = positiveSurvivors.filter(
  row => !(row[4] === 15 && row[5] >= 198)
);
const m214ZeroDesign = zeroBadRows.filter(
  row => row[2] + 1 - row[3] === 15 && row[1] - row[3] >= 198
);
const m214ZeroOther = zeroBadRows.filter(
  row => !(row[2] + 1 - row[3] === 15 && row[1] - row[3] >= 198)
);
insist(m214PositiveDesign.length === 659, 'positive design count');
insist(m214PositiveOther.length === 26, 'positive non-design count');
insist(m214ZeroDesign.length === 175, 'zero-bad design count');
insist(m214ZeroOther.length === 36, 'zero-bad terminal count');

function canonicalSet(rows) {
  return rows.map(row => JSON.stringify(row)).sort().join('\n');
}

const expectedPositiveSignatures = [];
for (let b = 149; b <= 154; ++b) {
  expectedPositiveSignatures.push([b, 213, 16, 1, 16, 212]);
}
for (let b = 149; b <= 160; ++b) {
  expectedPositiveSignatures.push([b, 214, 16, 1, 16, 213]);
}
for (let b = 149; b <= 154; ++b) {
  expectedPositiveSignatures.push([b, 214, 17, 2, 16, 212]);
}
expectedPositiveSignatures.push([149, 214, 18, 3, 16, 211]);
expectedPositiveSignatures.push([149, 214, 44, 31, 14, 183]);
const actualPositiveSignatures = m214PositiveOther.map(row => row.slice(0, 6));
insist(canonicalSet(actualPositiveSignatures) ===
       canonicalSet(expectedPositiveSignatures),
       'positive non-design signature ledger');

const expectedZeroSignatures = [];
for (let b = 149; b <= 153; ++b) expectedZeroSignatures.push([b, 212, 15, 0]);
for (let b = 149; b <= 160; ++b) expectedZeroSignatures.push([b, 213, 15, 0]);
for (let b = 149; b <= 167; ++b) expectedZeroSignatures.push([b, 214, 15, 0]);
const actualZeroSignatures = m214ZeroOther.map(row => row.slice(0, 4));
insist(canonicalSet(actualZeroSignatures) === canonicalSet(expectedZeroSignatures),
       'zero-bad terminal signature ledger');

// The exceptional integer-state scanner deliberately excludes the 659 design
// rows.  Its 34 states are the complete integer-feasible residue.
const expectedExceptionalSignatures = [];
for (let b = 149; b <= 154; ++b) {
  expectedExceptionalSignatures.push([b, 213, 16, 1, 16, 212, 1, 0]);
}
for (let b = 149; b <= 160; ++b) {
  expectedExceptionalSignatures.push([b, 214, 16, 1, 16, 213, 1, 0]);
}
for (let b = 149; b <= 154; ++b) {
  expectedExceptionalSignatures.push([b, 214, 17, 2, 16, 212, 2, 0]);
  expectedExceptionalSignatures.push([b, 214, 17, 2, 16, 212, 2, 1]);
}
expectedExceptionalSignatures.push([149, 214, 18, 3, 16, 211, 3, 0]);
for (let c = 455; c <= 457; ++c) {
  expectedExceptionalSignatures.push([149, 214, 44, 31, 14, 183, 101, c]);
}
const actualExceptionalSignatures = exceptionalIntegerStates.map(row =>
  [...row.slice(0, 6), row[7], row[8]]
);
insist(exceptionalIntegerStates.length === 34,
       'exceptional integer-state count is not 34');
insist(canonicalSet(actualExceptionalSignatures) ===
       canonicalSet(expectedExceptionalSignatures),
       'exceptional integer-state signature ledger');

// Every q=16 exceptional state is an exact DPW-equality deletion bridge to a
// good arrangement of degree 211, 212, or 213 and mdr 15.
for (const row of exceptionalIntegerStates) {
  const [marked, lines, relationDegree, bad, quotientDegree, good,
         goodDeficiency, badMarkedIncidence, markedBadPairs,
         residualBadGood, erasedUpper, slotCapacity, goodGoodDegree,
         lower, effectiveCap, parentCap, deletionCap] = row;
  if (quotientDegree === 14) {
    insist(marked === 149 && lines === 214 && relationDegree === 44 &&
           bad === 31 && good === 183 && badMarkedIncidence === 101 &&
           markedBadPairs >= 455 && markedBadPairs <= 457,
           'order-13 subplane exceptional state');
    insist(good === quotientDegree * (quotientDegree - 1) + 1,
           'order-13 subplane equality');
    continue;
  }
  insist(quotientDegree === 16 && relationDegree - bad === 15,
         'terminal deletion mdr');
  insist(Math.ceil(lower[0] / lower[1]) === deletionCap &&
         effectiveCap === deletionCap && parentCap >= deletionCap,
         'terminal deletion integer squeeze');
  const exactMarkedExcess =
    91 * marked - 13 * badMarkedIncidence + markedBadPairs;
  insist(deletionCap ===
         dpwBasic(good, 15) - pairs(good) - exactMarkedExcess,
         'terminal deletion exact marked excess');
  let survivingFifteenFold;
  if (badMarkedIncidence === 1 && markedBadPairs === 0) {
    survivingFifteenFold = marked - 1;
  } else if (badMarkedIncidence === 2 && markedBadPairs === 0) {
    survivingFifteenFold = marked - 2;
  } else if (badMarkedIncidence === 2 && markedBadPairs === 1) {
    survivingFifteenFold = marked - 1;
  } else if (badMarkedIncidence === 3 && markedBadPairs === 0) {
    survivingFifteenFold = marked - 3;
  } else {
    insist(false, 'unclassified terminal deletion incidence type');
  }
  insist(survivingFifteenFold >= good - 65,
         'terminal deletion fifteen-fold threshold');
  void goodDeficiency; void residualBadGood; void erasedUpper;
  void slotCapacity; void goodGoodDegree;
}

// Every B=0 residue is also squeezed to DPW equality with mdr 15.
for (const row of m214ZeroOther) {
  const [marked, lines, relationDegree, bad, gap] = row;
  const upper = dpwBasic(lines, relationDegree) - pairs(lines) - 91 * marked;
  const lowerNumerator = upper * gap[1] + gap[0];
  insist(bad === 0 && relationDegree === 15 && marked >= lines - 65,
         'zero-bad terminal geometry');
  insist(Math.ceil(lowerNumerator / gap[1]) === upper,
         'zero-bad terminal integer squeeze');
}

// Complete terminal moment audit.  The hostile minimization varies the actual
// number of epsilon=1 entries over its whole allowed interval; it does not
// merely test the lower endpoint.
const terminalSpecs = [
  [211, 146, [9735, 22294, 34853, 33489, 28561], 7648],
  [212, 147, [7132, 19901, 32670, 27889, 23409], 5040],
  [213, 148, [4773, 17754, 27225, 22801], 2676],
  [214, 149, [2664, 15859, 22201, 18225], 562]
];
const terminalLedger = [];
for (const [lines, minimumUnits, expectedDefectGaps,
            expectedDoubleGap] of terminalSpecs) {
  const tau = dpwBasic(lines, 15);
  const sumMuMinusOne = lines * (lines - 1) - tau;
  insist(sumMuMinusOne === 16 * lines - 241,
         'terminal sum(mu-1) identity');
  const epsilonBase = 3856 - 16 * lines;
  const epsilonSquareBase = lines * lines - 497 * lines + 61696;
  const defectGaps = [];
  for (let defect = 1; defect <= expectedDefectGaps.length; ++defect) {
    const pointCount = 241 - defect;
    const epsilonSum = epsilonBase - 15 * defect;
    const epsilonSquares = epsilonSquareBase - 225 * defect;
    let minimumGap = null;
    for (let units = minimumUnits; units <= pointCount; ++units) {
      const gap = (epsilonSum - units) ** 2 -
                  (pointCount - units) * (epsilonSquares - units);
      if (minimumGap === null || gap < minimumGap) minimumGap = gap;
    }
    insist(minimumGap > 0, 'terminal positive-defect Cauchy contradiction');
    defectGaps.push(minimumGap);
  }
  insist(JSON.stringify(defectGaps) === JSON.stringify(expectedDefectGaps),
         'terminal defect-gap ledger');
  insist(epsilonSquareBase -
         225 * (expectedDefectGaps.length + 1) < minimumUnits,
         'terminal larger-defect square-sum exclusion');
  let minimumDoubleGap = null;
  for (let units = minimumUnits; units <= 240; ++units) {
    const remainingSum = epsilonBase - 14 - units;
    const remainingSquares = epsilonSquareBase - 196 - units;
    const gap = remainingSum ** 2 - (240 - units) * remainingSquares;
    if (minimumDoubleGap === null || gap < minimumDoubleGap) {
      minimumDoubleGap = gap;
    }
  }
  insist(minimumDoubleGap === expectedDoubleGap,
         'terminal double-point gap');
  terminalLedger.push([
    lines, minimumUnits, tau, sumMuMinusOne,
    defectGaps, minimumDoubleGap
  ]);
}

const deployedCharacteristic = 2130706433;
insist(deployedCharacteristic > 214, 'deployed characteristic gate');
insist(13 % deployedCharacteristic !== 0,
       'order-13 subplane characteristic contradiction');
insist(15 % deployedCharacteristic !== 0,
       'terminal residue characteristic contradiction');

function rowDigest(rows) {
  return crypto.createHash('sha256')
    .update(canonicalSet(rows)).digest('hex');
}
const fullSurvivorDigest = rowDigest(positiveSurvivors);
const positiveOtherDigest = rowDigest(m214PositiveOther);
const exceptionalDigest = rowDigest(exceptionalIntegerStates);
const zeroOtherDigest = rowDigest(m214ZeroOther);

const output = [
  'M214_B149_FULL_ACTIVE_DELETION_NONEXISTENCE: PASS',
  'arithmetic_engine_sha256=' + BASE_SHA256,
  'field_characteristic=2130706433>214 domain=149<=b<=d<=214',
  'high_DPW_survivors=' + highRows.length,
  'coarse_rows=' + coarseRows.length +
    ' max_B=' + Math.max(...coarseRows.map(row => row[3])),
  'finite_space_cut=' + finiteSpaceCut.length +
    ' structural_rows=' + structuralRows.length,
  'B0_rows=' + zeroBadRows.length +
    ' Bpositive_rows=' + positiveBadRows.length,
  'joint_C_states=' + jointStateCount +
    ' joint_C_survivors=' + positiveSurvivors.length +
    ' least_positive_gap=' + leastPositiveJoint[0] + '/' + leastPositiveJoint[1],
  'design_positive=' + m214PositiveDesign.length +
    ' design_zero=' + m214ZeroDesign.length,
  'non_design_positive=' + m214PositiveOther.length +
    ' exceptional_integer_states=' + exceptionalIntegerStates.length +
    ' zero_bad_terminal=' + m214ZeroOther.length,
  'full_survivor_sha256=' + fullSurvivorDigest,
  'positive_other_sha256=' + positiveOtherDigest,
  'exceptional_state_sha256=' + exceptionalDigest,
  'zero_other_sha256=' + zeroOtherDigest,
  'terminal_ledger=' + JSON.stringify(terminalLedger),
  'q14_G183=equality_projective_plane_order13; char13_required',
  'terminal_residue=16=1 hence 15=0; impossible in char0 or char>214',
  'scope=arrangement_theorem_only; no recurrence_or_score_claim',
  'RESULT: PASS'
].join('\n') + '\n';

if (process.env.LEARN_OUTPUT === '1') {
  process.stdout.write(output);
  process.exit(0);
}
insist(M214_EXPECTED_SHA256 !== 'TO_BE_FROZEN',
       'canonical stdout hash not frozen');
const expectedPath = path.join(__dirname, M214_EXPECTED_BASENAME);
const expectedBytes = fs.readFileSync(expectedPath);
insist(crypto.createHash('sha256').update(expectedBytes).digest('hex') ===
       M214_EXPECTED_SHA256, 'canonical stdout hash drift');
insist(expectedBytes.equals(Buffer.from(output, 'utf8')),
       'canonical stdout byte mismatch');
process.stdout.write(output);
process.exit(0);
`;

replaceOnce(
  "insist(infeasibleRows.length === 0,\n       `joint-C rows with no relaxed state ${JSON.stringify(infeasibleRows.slice(0, 5))}`);",
  postScan,
  'frozen M214 post-scan verifier'
);

Function('require', '__dirname', 'process', 'BASE_SHA256',
         'M214_EXPECTED_SHA256', 'M214_EXPECTED_BASENAME', source)(
  require, __dirname, process, BASE_SHA256, EXPECTED_SHA256, EXPECTED_BASENAME
);
