import { useState } from "react";
import type { MetaFunction } from "@remix-run/node";

export const meta: MetaFunction = () => {
  return [
    { title: "Belote classement" },
    { name: "description", content: "Welcome to Remix!" },
  ];
};

export default function Index() {
  const [data, setData] = useState(null);
  const [imagePath, setImagePath] = useState("");

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/reconize", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ image_path: imagePath }),
      });
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      setData(data);
    } catch (error) {
      console.error("Erreur lors de la récupération des données:", error);
    }
  };

  return (
    <div className="font-sans p-4">
      <h1 className="text-2xl font-bold">Bienvenue à Belote classement</h1>
      <form onSubmit={handleSubmit} className="mt-4">
        <label className="block mb-2">
          Chemin de l&apos;image:
          <input
            type="text"
            value={imagePath}
            onChange={(e) => setImagePath(e.target.value)}
            className="border p-2 w-full"
          />
        </label>
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">
          Envoyer
        </button>
      </form>
      {data ? (
        <pre className="mt-4 p-4 bg-gray-100 rounded">
          {JSON.stringify(data, null, 2)}
        </pre>
      ) : (
        <p>Chargement des données...</p>
      )}
    </div>
  );
}
