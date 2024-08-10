import {
  Links,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@remix-run/react";
import Navbar from "./components/navbar";
import NotFound from "./components/404"; // Importer le composant NotFound
import "./tailwind.css";

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <Meta />
        <Links />
      </head>
      <body>
        <Navbar />
        {children}
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}

// Ajouter le composant ErrorBoundary
export function ErrorBoundary({ error }: { error: Error }) {
  console.error(error);

  return <NotFound />;
}

// Ajouter le composant CatchBoundary
export function CatchBoundary() {
  return (
      <NotFound />
  );
}

export default function App() {
  return <Outlet />;
}
