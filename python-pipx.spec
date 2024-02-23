# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pipx
Epoch: 100
Version: 1.7.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Install and run Python applications in isolated environments
License: MIT
URL: https://github.com/pypa/pipx/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
pipx is a tool to help you install and run end-user applications written
in Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and
Linux’s apt.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pipx
Summary: Install and run Python applications in isolated environments
Requires: python3
Requires: python3-argcomplete >= 1.9.4
Requires: python3-packaging >= 20.0
Requires: python3-platformdirs >= 2.1
Requires: python3-tomli
Requires: python3-userpath >= 1.6.0
Provides: pipx = %{epoch}:%{version}-%{release}
Provides: python3-pipx = %{epoch}:%{version}-%{release}
Provides: python3dist(pipx) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pipx = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pipx) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pipx = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pipx) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pipx
pipx is a tool to help you install and run end-user applications written
in Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and
Linux’s apt.

%files -n python%{python3_version_nodots}-pipx
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-pipx
Summary: Install and run Python applications in isolated environments
Requires: python3
Requires: python3-argcomplete >= 1.9.4
Requires: python3-packaging >= 20.0
Requires: python3-platformdirs >= 2.1
Requires: python3-tomli
Requires: python3-userpath >= 1.6.0
Provides: pipx = %{epoch}:%{version}-%{release}
Provides: python3-pipx = %{epoch}:%{version}-%{release}
Provides: python3dist(pipx) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pipx = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pipx) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pipx = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pipx) = %{epoch}:%{version}-%{release}

%description -n python3-pipx
pipx is a tool to help you install and run end-user applications written
in Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and
Linux’s apt.

%files -n python3-pipx
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n pipx
Summary: Install and run Python applications in isolated environments
Requires: python3
Requires: python3-argcomplete >= 1.9.4
Requires: python3-packaging >= 20.0
Requires: python3-platformdirs >= 2.1
Requires: python3-tomli
Requires: python3-userpath >= 1.6.0
Provides: pipx = %{epoch}:%{version}-%{release}
Provides: python3-pipx = %{epoch}:%{version}-%{release}
Provides: python3dist(pipx) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pipx = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pipx) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pipx = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pipx) = %{epoch}:%{version}-%{release}

%description -n pipx
pipx is a tool to help you install and run end-user applications written
in Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and
Linux’s apt.

%files -n pipx
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog