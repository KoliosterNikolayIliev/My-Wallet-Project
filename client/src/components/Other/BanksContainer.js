export const BanksContainer = ({ data }) => {
  if (data === []) return null;

  return (
    <div>
      <div className="banks-container">
        {data.map((bank) => {
          return (
            <div>
              <p>{bank.name}</p>
              <img src={bank.logo} width={100} />
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default BanksContainer;
