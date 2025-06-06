import React from 'react';

const AiSummary = ({ summary }) => (
  <div className="panel">
    <h3 className="panel-title">2. AI 摘要 & 问题提炼 (中文)</h3>
    <div className="ai-output">{summary || '等待处理工单...'}</div>
  </div>
);

export default AiSummary;
