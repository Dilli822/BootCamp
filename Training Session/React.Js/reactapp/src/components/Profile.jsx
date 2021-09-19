
//  for semantic ui
// functional com rfx
// component for profile Racher
import React from 'react'

export default function profile(props) {
    // checking the propos 
    // console.log(props.name)
    // console.log(props.profileprops)
    // destructing the props
    const {profileprops} = props;
    console.log(profileprops)


    // lets access the props
    return (
        <div className="ui list">
            <div className="item">
                <img  className="ul avaatar image" src={profileprops.img} alt="avatar" style={{ width: "50px",  borderRadius: "50%" }} />
                 <a href="https:/facebook.com/dilli822" className="header">
                     {/* accessing the props here name must be different coming from array  */}
                    {/* { props.profileprops.name} </a> */}
                    {/* Ram */}
                    {profileprops.name}
                    </a>
                 <div className="description"> 
                 {profileprops.description}
                    {/* Last Seen Watching Just Now. */}
                </div>            
            </div>
        </div>
    )
}
