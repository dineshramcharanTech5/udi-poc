package io.mosip.kernel.transliteration.translit.constant;

import com.asankha.translit.Transliterate;

public enum  LanguageIdConstant {

    SINHALA(Transliterate.SINHALA),
    TAMIL(Transliterate.TAMIL);

    /**
     * The language id.
     */
    private int languageId;

    /**
     * Constructor for LanguageIdConstant.
     *
     * @param languageId the language id.
     */
    LanguageIdConstant(int languageId) {
        this.languageId = languageId;
    }

    /**
     * Getter for language id.
     *
     * @return the language id.
     */
    public int getLanguage() {
        return languageId;
    }
}
