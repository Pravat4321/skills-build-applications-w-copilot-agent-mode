import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboards, setLeaderboards] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboards/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboards(results);
        console.log('Leaderboard API endpoint:', apiUrl);
        console.log('Fetched leaderboards:', results);
      });
  }, [apiUrl]);

  return (
    <div className="card p-4 mb-4">
      <h2 className="card-title text-success mb-3">Leaderboard</h2>
      <table className="table table-striped table-bordered">
        <thead>
          <tr>
            <th>Team</th>
            <th>Total Points</th>
          </tr>
        </thead>
        <tbody>
          {leaderboards.map((lb, idx) => (
            <tr key={lb.id || idx}>
              <td>{lb.team}</td>
              <td>{lb.total_points}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Leaderboard;
