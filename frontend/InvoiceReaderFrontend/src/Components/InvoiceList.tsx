import { useEffect, useState } from "react";
import List from "./List";
import "../InvoiceList.css";

type Invoice = {
  id: number;
  receiver: string;
  sender: string;
  dueDate: string;
  price: string;
  invoiceNumber: string;
};

function InvoiceList() {
  const [invoices, setInvoices] = useState<Invoice[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/invoices/")
      .then((res) => res.json())
      .then((data) => {
        setInvoices(data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  console.log(invoices);
  return (
    <div className="invoice-list-container">
      <div className="invoice-list">
        {invoices.map((f) => (
          <div key={f.id} className="list-item">
            <List
              receiver={f.receiver}
              sender={f.sender}
              invoiceNumber={f.invoiceNumber}
              price={f.price}
              dueDate={f.dueDate}
            />
          </div>
        ))}
      </div>
    </div>
  );
}

export default InvoiceList;
