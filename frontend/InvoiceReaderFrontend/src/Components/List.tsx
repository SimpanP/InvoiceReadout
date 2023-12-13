import React, { FC } from "react";

interface ListProps {
  receiver: string;
  sender: string;
  dueDate: string;
  price: string;
  invoiceNumber: string;
}

const List: FC<ListProps> = ({
  receiver,
  sender,
  dueDate,
  price,
  invoiceNumber,
}) => {
  return (
    <div>
      <p>Sender: {sender}</p>
      <p>Reciver: {receiver}</p>
      <p>Due date: {dueDate}</p>
      <p>Price: {price}</p>
      <p>Invoice Number: {invoiceNumber}</p>
    </div>
  );
};

export default List;
