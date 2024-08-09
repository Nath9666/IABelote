import { useState,useRef, useEffect } from "react";
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
  const [timestamp, setTimestamp] = useState(Date.now());
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    const startVideo = async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      } catch (error) {
        console.error("Erreur lors de l'accès à la caméra:", error);
      }
    };

    startVideo();
  }, []);

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
      setTimestamp(Date.now()); // Mettre à jour le timestamp pour recharger les images
    } catch (error) {
      console.error("Erreur lors de la récupération des données:", error);
    }
  };

  return (
    <div className="font-sans p-4">
      <h1 className="text-2xl font-bold">Bienvenue à Belote classement</h1>
      <form onSubmit={handleSubmit} className="mt-4">
        <p>Exemple : "./data/1_.png"</p>
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
        <>
          <article className="flex flex-wrap">
            <img
              src={`./public/data/original.png?timestamp=${timestamp}`}
              alt="Image 1"
              className="w-1/2 sd:w-full"
            />
            <img
              src={`./public/data/recognized.png?timestamp=${timestamp}`}
              alt="Image 2"
              className="w-1/2 sd:w-full"
            />
          </article>
          <pre className="mt-4 p-4 bg-gray-100 rounded">
            {JSON.stringify(data, null, 2)}
          </pre>
        </>
      ) : (
        <p>Chargement des données...</p>
      )}
      <div className="mt-4">
        <video ref={videoRef} autoPlay className="border p-2 w-full"></video>
      </div>
    </div>
  );
}
