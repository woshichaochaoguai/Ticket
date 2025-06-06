import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def _generate_content(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error calling Gemini API: {e}")
            return f"Error: Failed to get response from Gemini API. Details: {e}"

    def summarize_ticket(self, ticket_text):
        prompt = f"""
        你是一个专业的NAS技术支持专家。请仔细阅读以下多语言工单，并以清晰、结构化的方式用【中文】进行摘要。
        摘要应包含以下几个核心部分：
        1.  **发生了什么**：简述用户报告的事件或现象。
        2.  **核心问题**：提炼出用户最主要的诉求或遇到的技术难题。
        3.  **关键背景信息**：列出工单中提到的任何相关硬件型号、软件版本、网络环境、操作步骤等。

        工单原文如下：
        ---
        {ticket_text}
        ---
        请输出摘要：
        """
        return self._generate_content(prompt)

    def analyze_ticket(self, summary, kb_snippets):
        kb_context = "\n---\n".join(kb_snippets)
        prompt = f"""
        你是一个顶级的NAS故障排查专家。根据以下工单的中文摘要和相关的知识库参考信息，请用【中文】提供一份详细的分析和排查建议。
        你的分析应包含：
        1.  **可能原因分析**：基于摘要和知识库，列出导致问题的几种可能性。
        2.  **排查步骤建议**：提供清晰、可操作的步骤，指导技术支持工程师如何进一步定位问题。
        3.  **需要向用户确认的信息**：如果信息不足，列出需要向用户追问的问题。

        **工单摘要：**
        {summary}

        **相关知识库参考：**
        {kb_context}
        ---
        请输出你的分析与建议：
        """
        return self._generate_content(prompt)

    def generate_english_reply(self, analysis):
        prompt = f"""
        你是一名经验丰富的海外技术支持代表，擅长撰写专业、礼貌、清晰的英文邮件。
        请根据以下【中文】的内部问题分析和解决方案，草拟一封给客户的【英文】回复邮件/工单。

        邮件要求：
        - 语气：专业、有同理心、乐于助人。
        - 结构：
          1.  感谢用户并确认收到问题。
          2.  简要复述你对问题的理解，表明你在认真对待。
          3.  提出清晰的排查步骤或需要用户提供的信息（将中文步骤翻译成简单易懂的英文）。
          4.  结尾礼貌，并告知用户你会等待他的回复。
        - 格式：适合标准的工单或邮件回复。

        **内部中文分析：**
        {analysis}
        ---
        请草拟英文回复：
        """
        return self._generate_content(prompt)
