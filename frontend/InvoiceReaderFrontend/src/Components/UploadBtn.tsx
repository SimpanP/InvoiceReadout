// src/components/FileUpload.tsx
import React, { ChangeEvent, useState } from "react";
import axios from "axios";

const UploadBtn: React.FC = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    setSelectedFile(file);
  };

  const handleUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append("file", selectedFile);

      try {
        const response = await axios.post(
          "http://localhost:8000/api/upload/",
          formData
        );
        console.log(response.data);
      } catch (error) {
        console.error("Error uploading file:", error);
      }
    } else {
      console.error("No file selected");
    }
  };

  return (
    <div>
      <input
        type="file"
        accept=".pdf, .doc, .docx"
        onChange={handleFileChange}
      />
      <button onClick={handleUpload}>Upload</button>

      {selectedFile && (
        <div>
          {/* <p>Selected file: {selectedFile.name}</p>
          <p>File size: {selectedFile.size} bytes</p> */}
        </div>
      )}
    </div>
  );
};

export default UploadBtn;
