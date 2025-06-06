import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

import TicketInput from './components/TicketInput';
import AiSummary from './components/AiSummary';
import AiAnalysis from './components/AiAnalysis';
import EnglishReply from './components/EnglishReply';
import KnowledgeBase from './components/KnowledgeBase';

function App() {
  const [theme, setTheme] = useState('light');
  const [loading, setLoading] = useState(false);
  const [ticket, setTicket] = useState('');
  const [summary, setSummary] = useState('');
  const [kbResults, setKbResults] = useState([]);
  const [analysis, setAnalysis] = useState('');
  const [englishReply, setEnglishReply] = useState('');

  useEffect(() => {
    document.documentElement.className = theme;
  }, [theme]);

  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  const handleProcessTicket = async () => {
    setLoading(true);
    setSummary('');
    setKbResults([]);
    setAnalysis('');
    setEnglishReply('');
    try {
      const response = await axios.post('http://localhost:5001/api/process', { ticket });
      const { data } = response;
      setSummary(data.summary);
      setKbResults(data.knowledge_base_results);
      setAnalysis(data.analysis);
      setEnglishReply(data.english_reply);
    } catch (error) {
      console.error('Error processing ticket:', error);
      alert('处理失败: ' + (error.response?.data?.error || error.message));
    } finally {
      setLoading(false);
    }
  };

  const handleQuote = (kbText) => {
    setAnalysis(prev => prev + `\n\n[知识库引用]:\n${kbText}\n`);
  };

  return (
    <div className="app-container">
      {loading && <div className="loading-overlay">AI 正在全力分析中...</div>}

      <header className="header">
        <h1>海外NAS技术支持AI助手</h1>
        <button onClick={toggleTheme} className="button-secondary">
          切换到{theme === 'light' ? '暗黑' : '明亮'}模式
        </button>
      </header>

      <div className="left-panel">
        <TicketInput
          onProcess={handleProcessTicket}
          loading={loading}
          ticket={ticket}
          setTicket={setTicket}
        />
      </div>

      <div className="middle-panel">
        <AiSummary summary={summary} />
        <AiAnalysis analysis={analysis} setAnalysis={setAnalysis} />
        <EnglishReply reply={englishReply} setReply={setEnglishReply} />
      </div>

      <div className="right-panel">
        <KnowledgeBase results={kbResults} onQuote={handleQuote} />
      </div>
    </div>
  );
}

export default App;
