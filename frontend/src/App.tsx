import { Route, Routes } from "react-router-dom";

import HomePage from "../pages/HomePage";
import LoginPage from "../pages/LoginPage";
import RegisterPage from "../pages/RegisterPage";
import ProfilePage from "../pages/ProfilePage";
import NotFoundPage from "../pages/NotFoundPage";
import FeedPage from "../pages/FeedPage";
import "./App.css";
function App() {

  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/register" element={<RegisterPage />} />
      <Route path="/feed" element={<FeedPage />} />
      <Route path="/profile/:id" element={<ProfilePage />} />
      <Route path="/*" element={<NotFoundPage />} />
    </Routes>
  );
}

export default App;