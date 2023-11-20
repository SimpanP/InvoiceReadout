import React from "react";
import "../App.css";

const Navbar: React.FC = () => {
  return (
    <nav className="bg-[#9BA4B5] p-4 fixed top-0 w-full z-10">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-[#212A3E] text-4xl font-bold cursor-pointer">
          INVOICE
        </div>
        <div>
          <button className="rounded-md text-lg bg-[#394867] text-white font-medium py-3 px-6 lg:py-4 lg:px-8 font font-semibold">
            UPLOAD
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
