import { useEffect, useState } from "react";

export function useTest() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/test")
      .then(res => res.json())
      .then(setData)
      .catch(err => console.error(err));
  }, []);

  return data;
}
