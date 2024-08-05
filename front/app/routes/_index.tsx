import type { MetaFunction } from "@remix-run/node";
import { useEffect } from 'react';

export const meta: MetaFunction = () => {
  return [
    { title: "Belote classement" },
    { name: "description", content: "Welcome to Remix!" },
  ];
};

export default function Index() {
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/reconize');
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="font-sans p-4">
      <h1 className="text-2xl font-bold">Bienvenue à Belote classement</h1>
    </div>
  );
}
