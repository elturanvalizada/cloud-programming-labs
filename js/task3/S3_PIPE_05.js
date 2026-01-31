// S3_PIPE_05 — Log lines pipeline

function pipe(...fns) {
  return (input) => fns.reduce((v, fn) => fn(v), input);
}

const parseLines = (lines) =>
  lines.map(line => {
    const match = line.match(/^(\w+):\s*user=(\d+)$/);
    if (!match) return null;
    return { level: match[1], userId: Number(match[2]) };
  });

const onlyInfo = (records) =>
  records.filter(r => r && r.level === "INFO");

const extractUserIds = (records) =>
  records.map(r => r.userId);

const processLogs = pipe(parseLines, onlyInfo, extractUserIds);

// Tests
const lines = [
  "INFO: user=42",
  "WARN: user=7",
  "INFO: user=100",
  "BAD LINE",
  "INFO: user=3",
];

console.log(processLogs(lines)); // [42, 100, 3]
