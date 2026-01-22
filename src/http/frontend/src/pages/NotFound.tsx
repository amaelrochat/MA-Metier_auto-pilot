export default function NotFound() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-linear-to-br from-slate-50 to-slate-100">
      <div className="text-center">
        <h1 className="text-9xl font-bold text-slate-900 mb-4">404</h1>
        <p className="text-3xl font-semibold text-slate-700 mb-4">Page Not Found</p>
        <p className="text-lg text-slate-600 mb-8">Sorry, the page you're looking for doesn't exist.</p>
        <a
          href="/"
          className="inline-block px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg transition duration-300"
        >
          Go Back Home
        </a>
      </div>
    </div>
  );
}