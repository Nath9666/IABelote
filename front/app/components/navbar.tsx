import React from "react";

const Navbar: React.FC = () => {
  return (
    <nav className="bg-gray-800 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-white text-lg font-bold">Tournoi de Belote</div>
        <div className="flex space-x-4">
          <a href="/partie" className="text-gray-300 hover:text-white">
            Partie
          </a>
          <a href="/scan" className="text-gray-300 hover:text-white">
            Scan de feuille
          </a>
          <a href="/classement" className="text-gray-300 hover:text-white">
            Classement
          </a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
