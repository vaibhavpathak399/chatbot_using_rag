import "./SourceCard.css";

function SourceCard({ source }) {

  return (

    <div className="source-card">

      <div className="source-title">
        📄 {source.source}
      </div>

      <div className="source-page">
        Page {source.page}
      </div>

    </div>

  );
}

export default SourceCard;