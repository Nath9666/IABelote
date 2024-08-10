import { useState, useRef, useEffect } from "react";
import type { MetaFunction } from "@remix-run/node";

export const meta: MetaFunction = () => {
  return [
    { title: "Belote classement" },
    { name: "description", content: "Welcome to Remix!" },
  ];
};

const devBack = "http://127.0.0.1:5000";
const chemin_visible = false;

export default function Index() {
  const [data, setData] = useState(null);
  const [imagePath, setImagePath] = useState("");
  const [timestamp, setTimestamp] = useState(Date.now());
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const startVideo = async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          video: true,
        });
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      } catch (error) {
        console.error("Erreur lors de l'accès à la caméra:", error);
      }
    };

    startVideo();
  }, []);

  const handleSubmit = async (imagePath: string) => {
    try {
      const response = await fetch(devBack + "/reconize", {
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

  const clickButon = () => {
    handleSubmit(imagePath);
  };

  const captureImage = () => {
    if (videoRef.current && canvasRef.current) {
      const context = canvasRef.current.getContext("2d");
      if (context) {
        context.drawImage(
          videoRef.current,
          0,
          0,
          canvasRef.current.width,
          canvasRef.current.height
        );
        canvasRef.current.toBlob(async (blob) => {
          if (blob) {
            const formData = new FormData();
            formData.append("image", blob, "captured_image.png");

            try {
              const response = await fetch(devBack + "/upload", {
                method: "POST",
                body: formData,
              });

              if (response.ok) {
                console.log("Image uploaded successfully");
                console.log(JSON.stringify(response));
                setImagePath("./data/captured_image.png");
                handleSubmit(imagePath);
              } else {
                console.error("Failed to upload image");
              }
            } catch (error) {
              console.error("Error uploading image:", error);
            }
          }
        }, "image/png");
      }
    }
  };

  return (
    <div className="font-sans p-4">
      {chemin_visible ? (
        <>
          <h1 className="text-2xl font-bold">Bienvenue à Belote classement</h1>
          <div className="mt-4">
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
            <button
              className="bg-blue-500 text-white p-2 rounded"
              onClick={clickButon}
            >
              Envoyer
            </button>
          </div>
        </>
      ) : (
        <></>
      )}
      {data ? (
        <>
          <article className="flex flex-wrap">
            <img
              src={`./public/data/original.png?timestamp=${timestamp}`}
              alt="Original"
              className="w-1/2 sd:w-full"
            />
            <img
              src={`./public/data/recognized.png?timestamp=${timestamp}`}
              alt="Reconized"
              className="w-1/2 sd:w-full"
            />
          </article>
        </>
      ) : (
        <p>Chargement des données...</p>
      )}
      <div className="mt-4">
        <video ref={videoRef} autoPlay className="border p-2 w-full"></video>
        <button
          onClick={captureImage}
          className="bg-blue-500 text-white p-2 rounded mt-2"
        >
          Prendre une photo
        </button>
        <canvas
          ref={canvasRef}
          style={{ display: "none" }}
          width="640"
          height="480"
        ></canvas>
      </div>
    </div>
  );
}
