import { useState, useEffect, useRef } from "react";
import { sendMessage, getHistory } from "../services/api";
import ChatMessage from "../components/ChatMessage";
import ChatInput from "../components/ChatInput";
import ChatSidebar from "../components/ChatSidebar";
import "./ChatPage.css";

function ChatPage() {

  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState("");
  const [darkMode, setDarkMode] = useState(
  localStorage.getItem("theme") !== "light");
  const messagesEndRef = useRef(null);
  const [sidebarOpen, setSidebarOpen] = useState(
  localStorage.getItem("sidebar") !== "closed");

  useEffect(() => {

    const initializeChat = async () => {

      let existingSession =
        localStorage.getItem(
          "session_id"
        );

      if (!existingSession) {

        existingSession =
          crypto.randomUUID();

        localStorage.setItem(
          "session_id",
          existingSession
        );
      }

      setSessionId(
        existingSession
      );

      try {

        const history =
          await getHistory(
            existingSession
          );

        setMessages(
          history
        );

      } catch (error) {

        console.error(
          error
        );
      }
    };

    initializeChat();

  }, []);

  useEffect(() => {

    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth"
    });

  }, [messages]);

  const handleSend = async () => {

    if (!message.trim()) return;

    const userMessage = {
      role: "user",
      content: message
    };

    setMessages((prev) => [
      ...prev,
      userMessage
    ]);

    const currentMessage = message;

    setMessage("");

    try {

      setLoading(true);

      const result = await sendMessage(
        sessionId,
        currentMessage,
        messages
      );

      const botMessage = {
        role: "assistant",
        content: result.answer,
        sources: result.sources
      };

      setMessages((prev) => [
        ...prev,
        botMessage
      ]);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }
  };

return (

    <div
      className={
        darkMode
          ? "app dark"
          : "app light"
      }
    >

    <ChatSidebar sidebarOpen={sidebarOpen}/>

    <div className="chat-container">

      <div className="top-bar">

          <button
              className="menu-btn"
                onClick={() => {const nextState = !sidebarOpen;          
                setSidebarOpen(nextState);
                 localStorage.setItem(
                  "sidebar",
                  nextState ? "open" : "closed"
                );
              }}
              >
            ☰
          </button>

        <div className="theme-toggle">

          <button
              onClick={() => {
                const newTheme = !darkMode;
                setDarkMode(newTheme);
                localStorage.setItem(
                  "theme",
                  newTheme ? "dark" : "light"
              );
              }}
            >
            {darkMode
            ? "☀ Light"
            : "🌙 Dark"}
          </button>

        </div>

      </div>

      {messages.length === 0 && (
          <div className="hero">

            <div className="hero-icon">
               🤖
            </div>

            <h1>
              AI Knowledge Assistant
            </h1>

            <p>
              Ask anything from your documents
            </p>

        </div>

      )}

    {messages.length > 0 && (

    <div className="chat-box">

          {messages.map((msg,index)=>(

            <ChatMessage
              key={index}
              msg={msg}
             />

          ))}
          {loading && (
            <div className="typing">

              <span></span>
              <span></span>
              <span></span>

            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        )}

      <ChatInput
        message={message}
        setMessage={setMessage}
        handleSend={handleSend}
      />

    </div>

  </div>

);
}

export default ChatPage;