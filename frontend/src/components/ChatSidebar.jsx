import "./ChatSidebar.css";

function ChatSidebar({ sidebarOpen }) {

  return (
    

    <div className={ sidebarOpen ? "sidebar" : "sidebar collapsed"}>
      
      <div className="sidebar-logo">
        🤖 RAG AI
      </div>
    <button
      className="new-chat-btn"
      onClick={() => {

        const newSession =
          crypto.randomUUID();

        localStorage.setItem(
          "session_id",
          newSession
        );

        window.location.href = "/";
      }}
     >
        + New Chat
      </button>

      <div className="sidebar-title">
        Chat History
      </div>
      
      <div className="history-list">

        <div className="history-item">
          What is Python?
        </div>

        <div className="history-item">
        NIST Framework
        </div>

        <div className="history-item">
          Policy Questions
        </div>

      </div>

    </div>
    

  );
}

export default ChatSidebar;