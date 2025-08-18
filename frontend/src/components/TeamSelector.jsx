import Select from 'react-select';
import { teamData } from '../utils/teamUtils'

function TeamSelector({ label, name, value, onTeamChange }) {
    return (
    <div className={`select-${name}`}>
        <h1 className="team">{label}</h1>
        <label 
            htmlFor={name}
            style={{ fontSize: '16px'}}    
            >
                Choose a Team
        </label>
        <Select
        inputId={name}
            name={name}
            options={teamData}
            value={value}
            onChange={ (opt) => onTeamChange(opt) }
            isClearable
        />
    </div>
    );
}

export default TeamSelector;