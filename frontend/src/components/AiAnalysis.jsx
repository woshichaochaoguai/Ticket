import React from 'react';

const AiAnalysis = ({ analysis, setAnalysis }) => (
  <div className="panel">
    <h3 className="panel-title">3. AI 分析 & 建议 (可编辑)</h3>
    <textarea
      value={analysis}
      onChange={(e) => setAnalysis(e.target.value)}
      placeholder="AI分析建议将显示在此处..."
    />
  </div>
);

export default AiAnalysis;
