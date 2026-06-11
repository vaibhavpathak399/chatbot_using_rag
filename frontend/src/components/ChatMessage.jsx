import SourceCard from "./SourceCard";
import "./ChatMessage.css";

function ChatMessage({ msg }) {

  const isUser =
    msg.role === "user";

  return (

    <div
      className="message-wrapper"
      style={{
        display: "flex",
        justifyContent: isUser
          ? "flex-end"
          : "flex-start",
        marginBottom: "20px"
      }}
    >

      <div
        className={
          isUser
            ? "user-bubble"
            : "bot-bubble"
        }
      >
        <div className="message-role">
          {isUser
            ? "You"
            : "🤖 Assistant"}
        </div>

        <div className="message-content">
          {msg.content}
        </div>

        {msg.sources && (

        <div className="sources-section">

            <strong>
              Sources
            </strong>

            <div>

              {msg.sources.map(
                (
                  source,
                  idx
                ) => (

                  <SourceCard
                    key={idx}
                    source={source}
                  />

                )
              )}

            </div>

          </div>

        )}

      </div>

    </div>

  );
}

export default ChatMessage;