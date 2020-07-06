
import React from 'react';
import "./styles/ProgressBar.css";

export const ProgressBar =  ({width, percent}) => {
    const [value, setValue] = React.useState(0);

    React.useEffect(() => {
        setValue(percent * width);
    })

    return (
      <div className="progress-bar">
        <div className="progress-div" style={{width: width}}>
            <div 
              style={{width: `${value}px`}}
              className="progress"
            />
        </div>
      </div>
    )
}
