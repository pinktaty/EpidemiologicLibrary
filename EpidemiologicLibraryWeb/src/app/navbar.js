import {useContext, useState} from "react";
import {LanguageContext} from "@/app/language-context";
import Home from "@/app/home";
import ExploreData from "@/app/explore-data";
import AdditionalResources from "@/app/additional-resources";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faMagnifyingGlass} from "@fortawesome/free-solid-svg-icons";

export default function Navbar(){
    const {languageData} = useContext(LanguageContext);

    const [content, setContent] = useState("home");

    return (
        <div>
            <div className="m-5">
                <nav className="flex justify-center mt-1 mb-10 pt-2 pb-2">
                    <ul className="sm:inline-flex text-center text-lg">

                        <li className="md:ml-20 ml-2 sm:mr-20 mr-2 mb-6 sm:mb-0 navbar-button navbar-button-green bg-my-soft-blue"
                            onClick={() => setContent("home")}>{languageData.home.title}
                        </li>

                        <li className="md:pl-14 pl-4 sm:pr-14 pr-4 navbar-button navbar-button-yellow bg-blue-200"
                            onClick={() => setContent("explore-data")}>{languageData.exploreData.title}
                            <div className="ml-2">
                                <FontAwesomeIcon icon={faMagnifyingGlass}/>
                            </div>
                        </li>

                        <li className="md:ml-20 ml-2 sm:mr-20 mr-2 mt-6 sm:mt-0 navbar-button navbar-button-green bg-my-soft-blue"
                            onClick={() => setContent("additional-resources")}>{languageData.additionalResources.title}
                        </li>

                    </ul>
                </nav>

                <div className="m-7">
                    {content === 'home' && <Home/>}
                    {content === 'explore-data' && <ExploreData/>}
                    {content === 'additional-resources' && <AdditionalResources/>}
                </div>

            </div>
        </div>
    );
}