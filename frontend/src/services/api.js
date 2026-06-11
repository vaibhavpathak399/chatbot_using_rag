import axios from "axios";

const API_URL = "http://localhost:8000";

export const sendMessage = async (
  sessionId,
  message,
  history
) => {

  const response = await axios.post(
    `${API_URL}/chat`,
    {
      session_id: sessionId,
      message,
      history
    }
  );

  return response.data;
};
export const getHistory = async (
  sessionId
) => {

  const response = await axios.get(
    `${API_URL}/history/${sessionId}`
  );

  return response.data;
};