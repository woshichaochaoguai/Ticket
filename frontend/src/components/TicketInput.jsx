import React from 'react';

const TicketInput = ({ onProcess, loading, ticket, setTicket }) => (
  <div className="panel" style={{ height: 'calc(100% - 2rem)' }}>
    <h3 className="panel-title">1. 工单原文输入</h3>
    <textarea
      value={ticket}
      onChange={(e) => setTicket(e.target.value)}
      placeholder="在此处粘贴或输入工单原文..."
    />
    <div className="button-group">
      <button onClick={onProcess} disabled={loading || !ticket}>
        {loading ? '处理中...' : 'AI智能处理'}
      </button>
      <button className="button-secondary" onClick={() => setTicket('')}>清空</button>
    </div>
  </div>
);

export default TicketInput;
