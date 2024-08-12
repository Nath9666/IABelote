import { useState } from "react";
import { PlusCircleIcon, MinusCircleIcon } from "@heroicons/react/24/solid";

export default function Partie() {
  const [number, setNumber] = useState(0);
  const [participants, setParticipants] = useState(
    Array(number).fill({ nom: "", prenom: "", score: 0 })
  );
  const [dateDebut, setDateDebut] = useState("");
  const [dateFin, setDateFin] = useState("");

  const handleIncrement = () => {
    setNumber(number + 1);
  };

  const handleDesincrement = () => {
    setNumber(number - 1);
  };

  const handleParticipantChange = (
    index: number,
    field: string,
    value: string
  ) => {
    const newParticipants = [...participants];
    newParticipants[index] = { ...newParticipants[index], [field]: value };
    setParticipants(newParticipants);
  };

  const peopleInput = (index: number) => {
    const backgroundColor = index % 2 === 0 ? "bg-blue-100" : "bg-white";

    return (
      <div key={index} className={`p-4 flex flex-row gap-4 ${backgroundColor}`}>
        <div className="flex items-center justify-center w-1/10 h-16">
          {index}
        </div>
        <div className="flex flex-col flex-grow">
          <label
            htmlFor={`nom-${index}`}
            className="block text-gray-700 font-bold mb-2"
          >
            Nom
          </label>
          <input
            type="text"
            id={`nom-${index}`}
            name={`nom-${index}`}
            className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 mb-2"
            onChange={(e) =>
              handleParticipantChange(index, "nom", e.target.value)
            }
          />
        </div>
        <div className="flex flex-col flex-grow">
          <label
            htmlFor={`prenom-${index}`}
            className="block text-gray-700 font-bold mb-2"
          >
            Prénom
          </label>
          <input
            type="text"
            id={`prenom-${index}`}
            name={`prenom-${index}`}
            className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            onChange={(e) =>
              handleParticipantChange(index, "prenom", e.target.value)
            }
          />
        </div>
      </div>
    );
  };

  const saveTrournoi = async (
    Listparticipant: any,
    dateDebut: string,
    dateFin: string
  ) => {
    const devBack = "http://127.0.0.1:5000";

    //TODO: mettre les conditions pour envoyer dans la base en mettant les erreurs
    // dateDebut < dateFin
    // Listparticipant.length > 0
    // Listparticipant.length % 4 == 0

    try {
      const response = await fetch(devBack + "/saveTournoi", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          Listparticipant: Listparticipant,
          dateDebut: dateDebut,
          dateFin: dateFin,
        }),
      });
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      console.log("Données récupérées:", data);
    } catch (error) {
      console.error("Erreur lors de la récupération des données:", error);
    }
  };

  const handleButtonClick = () => {
    saveTrournoi(participants, dateDebut, dateFin);
    console.log(participants);
  };

  return (
    <div className="flex items-center justify-center my-8 border-gray-300">
      <div className="bg-white p-8 rounded shadow-md w-full">
        <h1 className="text-2xl font-bold mb-6 text-center">Nouveau Tournoi</h1>
        <div>
          <div className="flex flex-row items-center justify-center h-16 gap-8">
            <div className="cursor-pointer flex flex-grow items-center justify-center">
              <label
                htmlFor={`dateDebut`}
                className="flex flex-grow text-gray-700 font-bold"
              >
                Date de début
              </label>
              <input
                type="datetime-local"
                id={`dateDebut`}
                onChange={(e) => setDateDebut(e.target.value)}
                name={`dateDebut`}
                className="flex flex-grow px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div className="cursor-pointer flex flex-grow items-center justify-center">
              <label
                htmlFor={`dateFin`}
                className="flex flex-grow text-gray-700 font-bold"
              >
                Date de fin
              </label>
              <input
                type="datetime-local"
                id={`dateFin`}
                onChange={(e) => setDateFin(e.target.value)}
                name={`dateFin`}
                className="flex flex-grow px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
          </div>
          <div className="mb-4 hidden">
            <label
              htmlFor="participants"
              className="block text-gray-700 font-bold mb-2"
            >
              Nombre de participants
            </label>
            <input
              type="number"
              id="participants"
              name="participants"
              min="1"
              onChange={(e) => {
                const num = Number(e.target.value);
                setNumber(num);
                setParticipants(Array(num).fill({ nom: "", prenom: "", score:0}));
              }}
              className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Entrez le nombre de participants"
            />
          </div>
          {Array.from({ length: number }, (_, index) => peopleInput(index))}
          <div className="flex flex-row items-center justify-center h-16">
            <div
              className="cursor-pointer hover:bg-blue-100 w-1/2 flex items-center justify-center"
              onClick={handleIncrement}
            >
              <PlusCircleIcon className="h-6 w-6 text-blue-500" />
            </div>
            <div
              className="cursor-pointer hover:bg-blue-100 w-1/2 flex items-center justify-center"
              onClick={handleDesincrement}
            >
              <MinusCircleIcon className="h-6 w-6 text-blue-500" />
            </div>
          </div>
          <button
            onClick={handleButtonClick}
            className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Démarrer le tournoi
          </button>
        </div>
      </div>
    </div>
  );
}
