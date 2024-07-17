import {useContext} from "react";
import {LanguageContext} from "@/app/language-context";
import {faLink, faScrewdriverWrench, faDesktop} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

export default function AdditionalResources(){

    const {languageData} = useContext(LanguageContext);

    const resources = languageData.additionalResources;
    const sections = resources.sections;

    // TODO: Manejar un array de objetos, en vez de sólo los arrays. (Por mejorar).

    const loadSectionResources = (section) => {

        let sectionComponents = [];

        for (let i = 0; i < section.names.length; i++) {
            sectionComponents.push(
                <div className="m-3 mb-6 p-6 border-2 border-my-yellow rounded-3xl">
                    <h1 className="m-1 text-lg mb-2">
                        <FontAwesomeIcon icon={faScrewdriverWrench}/> {section.names[i]}
                    </h1>
                    <p className="m-3">{section.descriptions[i]}</p>
                    <p className="m-2">{resources.language}{section.languages[i]}</p>
                    <a className="m-2" href={section.links[i]}>link {<FontAwesomeIcon icon={faLink}/>}</a>
                </div>
            );
        }

        return sectionComponents;
    };

    const loadSection = (section) => {
        return(
            <div>
                <h1 className="flex text-2xl p-3 mb-6 border-b-2 border-b-my-green">
                    <div className="mr-2 text-my-green">
                        <FontAwesomeIcon icon={faDesktop}/>
                    </div>
                    {section.title}
                </h1>
                {loadSectionResources(section)}
            </div>
        );
    }

    const loadSections = () => {

        let sectionsLoaded = [];

        for (let i = 0; i < sections.length; i++) {
            sectionsLoaded.push(loadSection(sections[i]));
        }

        return sectionsLoaded;
    }

    return(
        <div className="text-center pb-4 pl-4 pr-4">
            {loadSections()}
        </div>
    );
}