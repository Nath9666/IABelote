export default function Partie() {
  return (
    <div className="flex items-center justify-center my-8 border-gray-300">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-sm">
        <h1 className="text-2xl font-bold mb-6 text-center">Nouvelle Partie</h1>
        <form>
          <div className="mb-4">
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
              className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Entrez le nombre de participants"
            />
          </div>
          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Démarrer la partie
          </button>
        </form>
      </div>
    </div>
  );
}