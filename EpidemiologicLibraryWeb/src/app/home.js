import {useContext} from "react";
import {LanguageContext} from "@/app/language-context";
import {faBiohazard, faAddressBook, faBullseye, faNewspaper} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

export default function Home(){
    const {languageData} = useContext(LanguageContext);

    const about = languageData.home.about;
    const contentAbout = about.content;

    const objectives = languageData.home.objectives;
    const contentObjectives = objectives.content;

    const news = languageData.home.news;
    const contentNews = news.content;

    const contact = languageData.home.contact;
    const contentContact = contact.content;
    const contactLinks = ["https://www.linkedin.com/in/diaz-lilith04", "https://carrerasconimpacto.org/"];

    const loadTitle = (title, icon) => {
        return (
            <h1 className="flex text-2xl p-3 mb-2 mt-2 border-b-2 border-b-my-green">
                <div className="mr-2 text-my-yellow">
                    <FontAwesomeIcon icon={icon}/>
                </div>
                {title}
            </h1>
        );
    }

    const loadContacts = () => {
        let contacts = [];

        for (let i = 0; i < contentContact.length; i++) {
            contacts.push(
                <p className="mt-3 flex justify-center whitespace-pre-wrap">
                    <span className="border-b-2 border-b-my-yellow">{contentContact[i][0]}</span>
                    <a href={contactLinks[i]} target="_blank">
                        {" " + contentContact[i][1]}
                    </a>
                </p>
            );
        }

        return contacts;
    }

    return (
        <div>
            <div className="m-2 mb-10">
                {loadTitle(about.title, faBiohazard)}
                <p className="mt-2">{contentAbout[0]}</p>
                <p className="mt-2">{contentAbout[1]}
                    <a href={"https://github.com/pinktaty/EpidemiologicLibrary"} target="_blank">
                        {contentAbout[2]}
                    </a>
                    {contentAbout[3]}
                </p>
            </div>
            <div className="m-2 mb-10">
                {loadTitle(objectives.title, faBullseye)}
                <p className="mt-2">{contentObjectives[0]}</p>
                <p className="mt-2">{contentObjectives[1]}</p>
            </div>
            <div className="m-2 mb-10">
                {loadTitle(news.title, faNewspaper)}
                <div className="m-6 p-6 text-center border-2 border-my-yellow rounded-md">
                <p>{contentNews[0]}</p>
                </div>
            </div>
            <div className="pt-10 pb-7 text-center">
                <h1 className="flex justify-center text-2xl">
                    {contact.title}
                    <div className="ml-2 text-my-green">
                        <FontAwesomeIcon icon={faAddressBook}/>
                    </div>
                </h1>
                {loadContacts()}
            </div>
        </div>
    );
}