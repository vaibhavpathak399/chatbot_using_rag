import { useState } from "react";
import { sendMessage } from "../services/api";

function ChatPage() {
  const [message, setMessage] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

const handleSend = async () => {
  try {
    setLoading(true);

    const result = await sendMessage(message);

    setAnswer(result.answer);

  } finally {
    setLoading(false);
  }
};

  return (
    <div>
      <h1>RAG Chatbot</h1>

      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      {loading ? <p>Thinking...</p> : <p>{answer}</p>}
      <button onClick={handleSend}>
        Send
      </button>

      <h3>Answer</h3>

      <p>{answer}</p>
    </div>
  );
}

export default ChatPage;