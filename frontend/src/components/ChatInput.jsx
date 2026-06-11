import "./ChatInput.css";

function ChatInput({
  message,
  setMessage,
  handleSend
}) {

  const handleKeyDown = (e) => {

    if (e.key === "Enter") {

      handleSend();
    }
  };

  return (

    <div className="chat-input-container">

      <input
        className="chat-input"
        type="text"
        placeholder="Ask anything..."
        value={message}
        onChange={(e) =>
          setMessage(
            e.target.value
          )
        }
        onKeyDown={(e) => {
        if (e.key === "Enter") {
          handleSend();
        }
      }}
      />

      <button
        className="send-btn"
        onClick={handleSend}
      >
        Send
      </button>

    </div>

  );
}

export default ChatInput;