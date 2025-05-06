import React from 'react';
import './Modal.css';

interface ModalProps {
  message: string;
  onClose: () => void;
}

const Modal: React.FC<ModalProps> = ({ message, onClose }) => {
  return (
    <div className="modal-backdrop">
      <div className="modal-box">
        <p>{message}</p>
        <button onClick={onClose}>Okay</button>
      </div>
    </div>
  );
};

export default Modal;
