export default function Layout({ children }) {
  return (
    <div className="app-container">
      <header className="topbar">
        AI Trading Intelligence Dashboard
      </header>

      <main className="main-content">
        {children}
      </main>
    </div>
  );
}