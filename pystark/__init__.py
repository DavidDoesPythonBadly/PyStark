# PyStark - Python add-on extension to Pyrogram
# Copyright (C) 2021-2022 Stark Bots <https://github.com/StarkBotsIndustries>
#
# This file is part of PyStark.
#
# PyStark is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyStark is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyStark. If not, see <https://www.gnu.org/licenses/>.


@ts-check

/**
 * @typedef {import("./client")} Client
 * @typedef {import("./types")} TelegramClient
 */

/**
 * @param {TelegramClient} client
 */
const idle = client => client.idle();

/**
 * @param {Client} client
 * @param {import("./types").AnyRequest} request
 */
const compose = (client, request) => client._compose(request);

module.exports = {
    compose,
    idle,
    raw,
    types,
    filters,
    handlers,
    emoji,
    enums,
    Client,
    StopTransmission,
    StopPropagation,
    ContinuePropagation,
    crypto_executor,
};
