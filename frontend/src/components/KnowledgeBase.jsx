import React from 'react';

const KnowledgeBase = ({ results, onQuote }) => (
  <div className="panel" style={{ height: 'calc(100% - 2rem)' }}>
    <h3 className="panel-title">知识库智能推荐</h3>
    <div style={{ overflowY: 'auto', flexGrow: 1 }}>
      {results.length === 0 && <p>暂无相关知识点。</p>}
      {results.map((item, index) => (
        <div key={index} className="kb-item">
          <button onClick={() => onQuote(item)}>引用</button>
          <p>{item}</p>
        </div>
      ))}
    </div>
  </div>
);

export default KnowledgeBase;
