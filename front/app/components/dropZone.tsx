// components/Dropzone.tsx
import React, { useCallback } from 'react';
import pkg from 'react-dropzone';
const { useDropzone } = pkg;

const Dropzone: React.FC = () => {
  const onDrop = useCallback((acceptedFiles: File[]) => {
    // Handle the files here
    console.log(acceptedFiles);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
        'image/png': ['.png'],
        'image/jpeg': ['.jpeg', '.jpg']
      },
    });

  return (
    <div
      {...getRootProps()}
      className={`border-2 border-dashed p-6 rounded-md text-center ${
        isDragActive ? 'border-blue-500' : 'border-gray-300'
      }`}
    >
      <input {...getInputProps()} />
      {isDragActive ? (
        <p>Déposez les fichiers ici...</p>
      ) : (
        <p>Glissez-déposez des fichiers ici, ou cliquez pour sélectionner des fichiers</p>
      )}
    </div>
  );
};

export default Dropzone;