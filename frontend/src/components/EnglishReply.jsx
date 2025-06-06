import React from 'react';

const EnglishReply = ({ reply, setReply }) => {
  const copyToClipboard = () => navigator.clipboard.writeText(reply);
  return (
    <div className="panel">
      <h3 className="panel-title">4. AI 英文回复草稿 (可编辑)</h3>
      <textarea
        value={reply}
        onChange={(e) => setReply(e.target.value)}
        placeholder="生成的英文回复将显示在此处..."
      />
      <div className="button-group">
        <button onClick={copyToClipboard} disabled={!reply}>复制回复</button>
      </div>
    </div>
  );
};

export default EnglishReply;
