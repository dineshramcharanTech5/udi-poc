package io.mosip.kernel.transliteration.translit.constant;

public enum  TransliterationErrorConstant {

    TRANSLITERATION_INVALID_ID("KER-TRL-SL-001", "Transliteration not possible for Translit engine"),
    TRANSLITERATION_INVALID_LANGUAGE_CODE("KER-TRL-SL-002", "Language code not supported for Translit engine");

    /**
     * The error code.
     */
    private String errorCode;

    /**
     * The error message.
     *
     */
    private String errorMessage;

    /**
     * Constructor for TransliterationErrorConstant.
     *
     * @param errorCode    the error code.
     * @param errorMessage the error message.
     */
    TransliterationErrorConstant(String errorCode, String errorMessage) {
        this.errorCode = errorCode;
        this.errorMessage = errorMessage;
    }

    /**
     * Getter for error code.
     *
     * @return the error code.
     */
    public String getErrorCode() {
        return errorCode;
    }

    /**
     * Getter for error message.
     *
     * @return the error message.
     */
    public String getErrorMessage() {
        return errorMessage;
    }

}
