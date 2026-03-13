import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const apiUrl = codespace
    ? `https://${codespace}-8000.app.github.dev/api/users/`
    : 'http://localhost:8000/api/users/';

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setUsers(results);
        console.log('Fetched users:', results);
        console.log('API endpoint:', apiUrl);
      })
      .catch(err => console.error('Erro ao buscar users:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2>Usuários</h2>
      <ul className="list-group">
        {users.map((u, idx) => (
          <li key={u.id || idx} className="list-group-item">
            {u.name} - {u.email}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Users;
