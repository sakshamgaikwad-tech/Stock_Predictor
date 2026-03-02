export default function RiskBadge({ level }) {
  let className = "risk-badge ";

  if (level.includes("Low")) className += "low";
  else if (level.includes("Medium")) className += "medium";
  else className += "high";

  return <span className={className}>{level}</span>;
}