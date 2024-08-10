import { useState } from "react";
import { PlusCircleIcon, MinusCircleIcon } from "@heroicons/react/24/solid";

export default function Partie() {
  const [number, setNumber] = useState(0);
  const [participants, setParticipants] = useState(
    Array(number).fill({ nom: "", prenom: "" })
  );

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

    const backgroundColor = index % 2 === 0 ? 'bg-blue-100' : 'bg-white';

    return (
      <div key={index} className={`mb-4 flex flex-row gap-4 ${backgroundColor}`}>
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

  return (
    <div className="flex items-center justify-center my-8 border-gray-300">
      <div className="bg-white p-8 rounded shadow-md w-full">
        <h1 className="text-2xl font-bold mb-6 text-center">Nouveau Tournoi</h1>
        <form>
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
                setParticipants(Array(num).fill({ nom: "", prenom: "" }));
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
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Démarrer le tournoi
          </button>
        </form>
      </div>
    </div>
  );
}
