import { useState } from "react";
import "./App.css";
import Home from "./pages/Home";
import WishlistPage from "./pages/WishlistPage";

/**
 * Root component of the application.
 *
 * Switches between the Home page and the Wishlist page using simple
 * local state, since this project only has two pages and doesn't need
 * a full router for that.
 */
function App() {
  const [page, setPage] = useState("home");

  if (page === "wishlist") {
    return <WishlistPage onBack={() => setPage("home")} />;
  }

  return <Home onOpenWishlist={() => setPage("wishlist")} />;
}

export default App;