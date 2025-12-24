import { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    {
      sender: "ai",
      text: "Hello 👋 I can provide general health information. How can I help you today?"
    }
  ]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages(prev => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const response = await fetch(
        "https://ai-health-assistant.onrender.com/chat", // ✅ YOUR LIVE BACKEND
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: userMessage.text })
        }
      );

      const data = await response.json();

      setMessages(prev => [
        ...prev,
        { sender: "ai", text: data.reply }
      ]);
    } catch (error) {
      setMessages(prev => [
        ...prev,
        { sender: "ai", text: "⚠️ Server error. Please try again." }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-900 via-purple-900 to-black">

      <div className="w-full max-w-4xl h-[85vh] rounded-2xl 
                      bg-white/10 backdrop-blur-xl 
                      border border-white/20 
                      shadow-2xl flex flex-col">

        {/* Header */}
        <div className="px-6 py-4 border-b border-white/20 flex items-center justify-between">
          <h1 className="text-white text-xl font-semibold tracking-wide">
            🩺 AI Health Assistant
          </h1>
          <span className="text-sm text-white/70">
            Safe • Informative • AI-Powered
          </span>
        </div>

        {/* Chat Area */}
        <div className="flex-1 p-6 space-y-4 overflow-y-auto">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`max-w-md px-4 py-3 rounded-2xl shadow-md text-white
                ${msg.sender === "user"
                  ? "ml-auto bg-gradient-to-r from-blue-500 to-indigo-500"
                  : "bg-white/20 backdrop-blur-md"
                }`}
            >
              {msg.text}
            </div>
          ))}

          {loading && (
            <div className="max-w-md bg-white/20 backdrop-blur-md 
                            text-white px-4 py-3 rounded-2xl shadow-md">
              AI is thinking…
            </div>
          )}
        </div>

        {/* Input Area */}
        <div className="p-4 border-t border-white/20">
          <div className="flex gap-2">
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              type="text"
              placeholder="Ask a health-related question..."
              className="flex-1 px-4 py-3 rounded-xl 
                         bg-white/20 backdrop-blur-md 
                         text-white placeholder-white/60 
                         outline-none border border-white/20
                         focus:ring-2 focus:ring-indigo-400"
            />

            <button
              onClick={sendMessage}
              className="px-6 py-3 rounded-xl font-medium text-white
                         bg-gradient-to-r from-indigo-500 to-blue-500
                         hover:scale-105 transition-transform shadow-lg">
              Send
            </button>
          </div>
        </div>

      </div>
    </div>
  );
}

export default App;
