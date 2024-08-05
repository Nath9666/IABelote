import type { MetaFunction } from "@remix-run/node";
import { Link } from "@remix-run/react";
import Dropzone from "../components/dropZone";

export const meta: MetaFunction = () => {
  return [
    { title: "Belote classement" },
    { name: "description", content: "Welcome to Remix!" },
  ];
};

export default function Index() {
  return (
    <div className="font-sans p-4">
      <h1 className="text-2xl font-bold">Bienvenue à Belote classement</h1>
    </div>
  );
}