$(() => {
    $('#cipher-input').on('input', function() {
        clearInputError($(this), $('#cipher-helper'));
    });

    $('#cipher-reset').on('click', () => {
        clearInputError($('#cipher-input'), $('#cipher-helper'));
    });

    $('#cipher-submit').on('click', () => {
        const input = $('#cipher-input');
        const val = String(input.val()).trim();
        if (val === '') {
            setInputError(input, $('#cipher-helper'), 'Input required');
        }
        else if (!isHex(val)) {
            setInputError(input, $('#cipher-helper'), 'Hex format required');
        }
        else if (val.length % 2 !== 0) {
            setInputError(input, $('#cipher-helper'), 'Input cannot be of odd length');
        }
        else {
            $('#cipher-form').hide().trigger('reset');
            setTimeout(() => {
                const table = buildTable(parseHex(val));
                $('#table-container').append(table);
            }, 1);
        }
    });
});

const setHint = (helperEl, msg) => {
    helperEl.text(msg);
};

const setInputError = (inputEl, helperEl, msg) => {
    inputEl.attr('aria-invalid', 'true');
    setHint(helperEl, msg);
};

const clearInputError = (inputEl, helperEl) => {
    inputEl.removeAttr('aria-invalid');
    setHint(helperEl, '');
};

/** @type {(str: string) => boolean} */
const isHex = (str) => {
    return /^[0-9a-fA-F]*$/.test(str)
};

/** @type {(hex: string) => number[]} */
const parseHex = (hex) => {
    results = [];
    for (i = 0; i < hex.length; i += 2) {
        code = parseInt(hex.substring(i, i + 2), 16);
        results.push(code);
    }
    return results;
};

/** @type {(byteArr: number[]) => str} */
const buildTable = (byteArr) => {
    const header = buildHeader(byteArr.length);
    let codeRow = '';
    let charRow = '';
    let inputRow = '';
    let displayRow = '';
    byteArr.forEach((code) => {
        const char = String.fromCharCode(code);
        codeRow += `<td>${code}</td>`;
        charRow += `<td>${char}</td>`;
        inputRow += `<td><input type="text" maxlength="1" placeholder="${char}"></td>`;
        displayRow += `<td><input type="text" value="${char}" readonly></td>`
    });
    const table = $(
        `<table>${header}<tbody><tr id="code-row">${codeRow}</tr><tr>${charRow}</tr><tr id="input-row">${inputRow}</tr><tr id="display-row">${displayRow}</tr></tbody></table>`);
    table.find('#input-row').on('input', function (e) {
        const newVal = e.target.value;
        const index = $(this).children().index($(e.target).parent());
        const code = Number(table.find('#code-row').children().eq(index).text());
        const display = table.find('#display-row').find('input').eq(index);
        display.val(String.fromCharCode(newVal !== '' ? newVal.charCodeAt(0) ^ code : code))
    });
    return table;
}

/** @type {(byteArr: number) => string} */
const buildHeader = (len) => `<thead><tr>${Array.from(Array(len).keys()).reduce((acc, cur) => acc + `<th>${cur}</th>`, '')}</tr></thead>`
